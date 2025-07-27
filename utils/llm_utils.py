import datetime
import lmstudio as lms

lm_studio_host = None
# lm_studio_host = "192.168.1.29:1234"
# lms.configure_default_client(lm_studio_host)
# print(lms.get_default_client())

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


# TEST
# RunUtility.list_downloaded_models(lm_studio_host)
# RunUtility.get_loaded_models(lm_studio_host)
# RunUtility.get_server_address(lm_studio_host)


# PRINT FUCNCTIONS
# print(RunUtility.get_server_address(lm_studio_host))
# print(RunUtility.get_loaded_models(lm_studio_host))
# print(RunUtility.list_downloaded_models(lm_studio_host))


# OBJECT TYPES
# # # print(type(RunUtility.get_server_address(lm_studio_host)))
# # # print(type(RunUtility.get_loaded_models(lm_studio_host)))
# # # print(type(RunUtility.list_downloaded_models(lm_studio_host)))




# # get current model
# def get_current_model():
#     model = lms.llm()
#     print(model)
#     return model
#     # retrun model
#     # print('Current model')

# # Unload model
# def unload_model():
#     try:
#         print('Unloading model')
#         model = lms.llm()
#         model.unload()
#         print('model unloaded')
#     except:
#         print(check_model())

# # Check model
# def check_model():
#     try:
#         model = lms.llm()
#         print(model)
#     except Exception as e:
#         print(e)

# def load_model():
#     model = lms.llm("deepseek/deepseek-r1-0528-qwen3-8b")
#     print(get_current_model())
#     print(lms.llm)



