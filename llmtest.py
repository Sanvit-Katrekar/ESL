import replicate
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['REPLICATE_API_TOKEN'] = os.getenv('REPLICATE_API_TOKEN')
output = replicate.run(
    "meta/llama-2-7b-chat:ac944f2e49c55c7e965fc3d93ad9a7d9d947866d6793fb849dd6b4747d0c061c",
    input={"prompt": "Hi"}
)
# The meta/llama-2-7b-chat model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    # https://replicate.com/meta/llama-2-7b-chat/versions/ac944f2e49c55c7e965fc3d93ad9a7d9d947866d6793fb849dd6b4747d0c061c/api#output-schema
    print(item, end="")