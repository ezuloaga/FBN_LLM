import datetime
import lmstudio as lms

lm_studio_host = None


class RunUtility:

    def __init__(self, lm_studio_host):
        self.lm_studio_host = lm_studio_host

    lms.configure_default_client(lm_studio_host)
    ts = datetime.datetime.now()
    # print(ts)

    # Get LM Studio Host
    def get_server_address(lm_studio_host):
        error_msg = None
        try:
            client = lms.get_default_client()
            lm_server_host = client.api_host
            return lm_server_host
        except Exception as e:
            error_msg = str(e)
            return error_msg

    # List Loaded Models
    def get_loaded_models(lm_studio_host):
        error_msg = None
        try:
            all_loaded_models = lms.list_loaded_models()
            return all_loaded_models
        except Exception as e:
            error_msg = str(e)
            return error_msg

    # List available (downloaded) models
    def list_downloaded_models(lm_studio_host):
        try:
            downloaded = lms.list_downloaded_models()
            for model in downloaded:
                print(model)
            else:
                pass
        except Exception as e:
            error_msg = str(e)
            return error_msg
