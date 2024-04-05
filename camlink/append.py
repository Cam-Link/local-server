import os
import subprocess

class Command(BaseCommand):
    help = 'Concatenate videos'

    def handle(self, *args, **options):
        
        folder_path = '/path/to/videos/folder'

        output_file = '/path/to/output/video.mp4'

       
        video_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith('.mp4')]

        if len(video_files) > 0:
            ffmpeg_command = ['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'filelist.txt', '-c', 'copy', output_file]
            with open('filelist.txt', 'w') as filelist:
                for video_file in video_files:
                    filelist.write(f"file '{video_file}'\n")
            subprocess.run(ffmpeg_command)

        
        if os.path.exists('filelist.txt'):
            os.remove('filelist.txt')