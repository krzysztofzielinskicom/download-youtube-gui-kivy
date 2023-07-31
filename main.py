from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from pytube import YouTube
import os

class YouTubeDownloaderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        self.url_input = TextInput(hint_text='Enter YouTube URL', multiline=False)
        layout.add_widget(self.url_input)

        self.path_input = TextInput(hint_text='Enter path to store file', multiline=False)
        layout.add_widget(self.path_input)

        download_button = Button(text='Download', on_press=self.download_button_clicked)
        layout.add_widget(download_button)

        self.status_label = Label(text='', size_hint=(1, None), height=44)
        layout.add_widget(self.status_label)

        return layout

    def downloadYoutube(self, vid_url, path):
        try:
            yt = YouTube(vid_url)
            yt_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            if not os.path.exists(path):
                os.makedirs(path)
            yt_stream.download(path)
            self.status_label.text = "Download completed!"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"
    def download_button_clicked(self, instance):
        url = self.url_input.text
        path = self.path_input.text
        self.downloadYoutube(url, path)

if __name__ == '__main__':
    YouTubeDownloaderApp().run()
