import os
import dropbox
import json

class DropboxHandler:
    def __init__(self, api_key, dropbox_path):
        self.dbx = dropbox.Dropbox(api_key)
        self.dropbox_path = dropbox_path

    def get_files_in_folder(self):
        response = self.dbx.files_list_folder(self.dropbox_path)
        return [os.path.splitext(entry.name)[0] for entry in response.entries]

    def upload_file(self, file_path):
        with open(file_path, "rb") as f:
            fullpath = f"{self.dropbox_path}/{file_path}"
            self.dbx.files_upload(f.read(), fullpath)
        print(f"File {file_path} uploaded.")

    def upload_metadata(self, metadata, file_name):
        metadata_path = f"{self.dropbox_path}/{file_name}.json"
        self.dbx.files_upload(json.dumps(metadata).encode(), metadata_path)
        print("Metadata uploaded.")
    
    def download_file_from_dropbox(self, filename):
        fullpath = f"{self.dropbox_path}/{filename}.json"
        _, res = self.dbx.files_download(fullpath.replace("#", "|"))
        return json.loads(res.content)
    
    def get_data_refined(self):
        result = self.dbx.files_list_folder(self.dropbox_path)
        data_result = {}
    
        for entry in result.entries:
            if isinstance(entry, dropbox.files.FileMetadata) and entry.name.lower().endswith(".mp3"):
                links = self.dbx.sharing_list_shared_links(entry.path_lower).links
                if links:
                    shared_link = links[0].url
                else:
                    shared_link = self.dbx.sharing_create_shared_link_with_settings(entry.path_lower).url
                
                shared_link = shared_link[:-5] + "?raw=1"
                
                data = self.download_file_from_dropbox(entry.name.replace(".mp3", ""))
                data_result[shared_link] = data 

        return data_result
