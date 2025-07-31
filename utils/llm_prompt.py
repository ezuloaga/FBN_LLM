import lmstudio as lms


user_prompt = None
lm_studio_host = None
model_to_use = None


def text_prompt(user_prompt,lm_studio_host,model_to_use):
    try:
        lms.configure_default_client(lm_studio_host)
        model = lms.llm(model_to_use)
        result = model.respond(user_prompt)
        model_used = result.model_info.display_name
        predicted_tokens = result.stats.predicted_tokens_count
        ttft = result.stats.time_to_first_token_sec
        stop_reason = result.stats.stop_reason

    except Exception as e:
        print(e)
        return e

    return result, model_used, predicted_tokens, ttft, stop_reason


def describe_image_prompt(user_prompt,lm_studio_host,model_to_use,image_file):
    try:
        lms.configure_default_client(lm_studio_host)
        model = lms.llm(model_to_use)
        image_handle = lms.prepare_image(image_file)
        chat = lms.Chat()
        chat.add_user_message(user_prompt, images=[image_handle])
        prediction = model.respond(chat)
        return prediction
    except Exception as e:
        print(e)
        return e
