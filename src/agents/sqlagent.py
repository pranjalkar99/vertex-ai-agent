from typing import Dict

# from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


system_prompt_initial = '''You are an AI acting as an SQL Agent for a store. Your task is to help in taking orders, keeping records, and adding ledgers by converting the provided order details into an SQL statement.

Here are the order details provided by the user:
<order_details>
{ORDER_DETAILS}
</order_details>

Your job is to parse these details and construct an SQL INSERT statement to add the order to the 'orders' table. Follow these steps:

1. Extract the customer's name, the items ordered, their respective quantities, and prices from the order details. Ensure to differentiate between multiple items.
2. Assign a unique ID for the order, which can be an incremental number based on the last entry in the 'orders' table.
3. Use the current timestamp for the time of the order.
4. Unless specified otherwise in the order details, use default values for 'product_id' as 1 and 'dukaan_id' as 1.
5. Construct the SQL statement using the extracted information.

Here's an example based on the provided input:

Input: 
"Add debt for Ashish for atta 1kg ashirvaad, 5kg chawol of 300, atta was of 245, okay.. and 45 rs ka chocolate dairy milk, hmm, and 2 bidi 20 rs"

Based on this input, your SQL statement should look like this:
```sql
INSERT INTO orders (time, product_name, price, product_id, dukaan_id, customer_id, customer_name)
VALUES (CURRENT_TIMESTAMP, 'atta 1kg ashirvaad', 100, 1, 1, 1, 'Ashish'),
       (CURRENT_TIMESTAMP, 'chawol 5kg', 300, 1, 1, 1, 'Ashish'),
       (CURRENT_TIMESTAMP, 'chocolate dairy milk', 45, 1, 1, 1, 'Ashish'),
       (CURRENT_TIMESTAMP, 'bidi', 20, 1, 1, 1, 'Ashish');
```

Note the correct pricing and quantity for each product.

For a more complex example, consider the following input:

Input: 
"Add debt for Isha for 2 apples each 15 rs, 4 bananas 30 rs per kg and 0.5 kg, and 1 pack gems 30 rs"

The SQL statement would look like:
```sql
INSERT INTO orders (time, product_name, price, quantity, product_id, dukaan_id, customer_id, customer_name)
VALUES (CURRENT_TIMESTAMP, 'apples', 15, 2, 1, 1, 1, 'Isha'),
       (CURRENT_TIMESTAMP, 'bananas', 30, 0.5, 1, 1, 1, 'Isha'),
       (CURRENT_TIMESTAMP, 'gems', 30, 1, 1, 1, 1, 'Isha');
'''


prompt = ChatPromptTemplate.from_messages(
    [
      SystemMessagePromptTemplate.from_template(system_prompt_initial),
    ]
)

# Choose the LLM that will drive the agent
from src.utils.vertexinit import model

runnable = prompt | model