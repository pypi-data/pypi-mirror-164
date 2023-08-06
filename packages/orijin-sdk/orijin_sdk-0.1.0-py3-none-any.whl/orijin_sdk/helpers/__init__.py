import requests             # Image Uploading

#region: Image Uploading
def upload_image(file_path, endpoint, token):
    """Use GQL mutation.fileUpload
    
    Args:
        file_path (string): The path of the file to be uploaded.
    
    Returns:
        name, url
    """
    with open(file_path, 'rb') as upload_file:
        # url = endpoint

        headers = {
            'Authorization': token,
            'Content-Type': 'multipart/form-data',
        }

        form = {
            'operations': (None, "{\"query\": \"mutation ($file: Upload!) {fileUpload(file: $file) {name, url}}\", \"variables\": { \"file\": null }}"),
            'map': (None, "{\"0\":[\"variables.file\"]}"),
            '0': ("0", upload_file, "image/jpeg")
        }

        response = requests.post(url=endpoint, headers=headers, files=form)

        # # DEBUGGING: Uncomment this to print the request to a file (similar to saving a network request in Chrome) for review.
        # with open('temp/request.txt','w') as request_file:
        #     request_file.write('{}\n{}\r\n{}\r\n\r\n{}'.format(
        #         '-----------START-----------',
        #         response.request.method + ' ' + response.request.url,
        #         '\r\n'.join('{}: {}'.format(k, v) for k, v in response.request.headers.items()),
        #         response.request.body,
        #     ))

        return(response.text)
#endregion
