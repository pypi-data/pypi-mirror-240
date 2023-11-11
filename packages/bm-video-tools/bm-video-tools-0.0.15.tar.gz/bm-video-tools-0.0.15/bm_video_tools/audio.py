from __future__ import annotations
import asyncio
import json
from moviepy.editor import AudioFileClip, concatenate_audioclips, CompositeAudioClip

from .operate import Operate

from .utils.utils import backslash2slash, get_fmt, make_output_dirs
from .utils.async_utils import async_subprocess_exec, async_pre_operate_batch


class Audio:
    def __init__(self, input_path: str):
        self.input_path = backslash2slash(input_path)
        self.fmt = get_fmt(self.input_path)

    async def get_info(self) -> dict:
        """
        查看媒体信息
        :return: 媒体详细信息
        """
        cmd = r'ffprobe -i {} -v error -show_format -show_streams -print_format json'
        res = await async_subprocess_exec(cmd, self.input_path)
        return json.loads(res)

    async def run(self, op: Operate, output_path: str) -> Audio:
        """
        执行操作
        :param op: Operation实例对象
        :param output_path: 输出路径
        :return: 媒体对象
        """
        output_path = backslash2slash(output_path)
        make_output_dirs(output_path)

        cmd = op.exec(o_a=True)
        await async_subprocess_exec(cmd, self.input_path, output_path)

        return self.__class__(output_path)

    @staticmethod
    @async_pre_operate_batch(("Audio",))
    async def concat(output_path: str, audio_list: list, logger: bool = False) -> Audio:
        """
        音频拼接
        :param output_path: 输出路径
        :param audio_list: 音频列表
        :param logger: 是否打印进度
        :return: 音频对象
        """
        output_path = backslash2slash(output_path)
        make_output_dirs(output_path)

        def _content():
            clips = []
            final_clip = None
            try:
                for item in audio_list:
                    media = item["media"]
                    clips.append(AudioFileClip(media.input_path))

                final_clip = concatenate_audioclips(clips)
                final_clip.write_audiofile(output_path, logger='bar' if logger else None)
            finally:
                # 释放资源
                for clip in clips:
                    clip.close()
                if final_clip:
                    final_clip.close()

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, _content)

        return Audio(output_path)

    @staticmethod
    @async_pre_operate_batch(("Audio",))
    async def composite(output_path: str, audio_list: list, logger: bool = False) -> Audio:
        """
        音频合成
        :param output_path: 输出路径
        :param audio_list: 音频列表
        :param logger: 是否打印进度
        :return: 音频对象
        """
        output_path = backslash2slash(output_path)
        make_output_dirs(output_path)

        def _composite():
            clips = []
            final_clip = None
            try:
                for item in audio_list:
                    media = item["media"]

                    clip = AudioFileClip(media.input_path)
                    if "start" in item:
                        clip = clip.set_start(item.get("start"))
                    if "end" in item:
                        clip = clip.set_end(item.get("end"))

                    clips.append(clip)

                final_clip = CompositeAudioClip(clips)
                final_clip.fps = 44100
                final_clip.write_audiofile(output_path, logger='bar' if logger else None)
            finally:
                # 释放资源
                for clip in clips:
                    clip.close()
                if final_clip:
                    final_clip.close()

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, _composite)

        return Audio(output_path)
