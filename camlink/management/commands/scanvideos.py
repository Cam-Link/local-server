import os
from django.core.management.base import BaseCommand
from camlink.models import Video
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
    help = 'Scan and upload videos'

    def handle(self, *args, **options):
        # Get the admin user
        admin_user = User.objects.get(username='admin')

        # Create the folder to store videos if it doesn't exist
        folder_path = os.path.join(settings.MEDIA_ROOT, 'videos')
        os.makedirs(folder_path, exist_ok=True)
        
        # Create the folder to append videos if it doesn't exist
        append_folder_path = os.path.join(settings.MEDIA_ROOT, 'appended_videos')
        os.makedirs(append_folder_path, exist_ok=True)

        # Scan the folder for new video files
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Create a Video instance for each new video file
            video = Video(file=file_path, uploaded_by=admin_user)
            video.save()
            
            
            new_file_path = os.path.join(append_folder_path, filename)
            os.rename(file_path, new_file_path)