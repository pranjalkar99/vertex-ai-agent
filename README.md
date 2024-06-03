# Hackathon Project: Vertex AI SQL Agent for Shop Management

## Project Overview

The aim of this project is to develop an AI-powered SQL agent using Google's Vertex AI Agent Builder. This agent will convert spoken text, obtained using a Speech-to-Text (STT) model, into corresponding SQL commands. These commands will be used to manage and maintain records of shop purchases, ledgers, debts, and more. The target users are small shopkeepers who may find it challenging to manually enter each record in a busy day of customer purchases but still want to maintain comprehensive records for tax and analysis purposes.

## Problem Statement

Small shopkeepers often struggle with maintaining detailed records of their transactions due to the manual effort required, especially during peak business hours. This can lead to inaccurate financial records, difficulties in tracking debts, and challenges in preparing for tax filings. Additionally, maintaining accurate records is crucial for analyzing sales trends and managing inventory.

## Solution

Our solution leverages the capabilities of Vertex AI to create an intelligent agent that can:
1. Convert spoken order details into SQL commands.
2. Automatically update the shop's database with purchase records, debts, and ledgers.
3. Facilitate easy management of financial records without the need for manual entry.

### Key Features

- **Speech-to-Text Integration**: Convert spoken order details into text using a Speech-to-Text (STT) model.
- **Automated SQL Generation**: Parse the text and generate SQL INSERT statements to update the shop's database.
- **Customer Management**: Check for existing customers and retrieve their customer IDs or create new customer entries as needed.
- **Real-Time Updates**: Use the current timestamp for order entries.
- **Default Values**: Apply default values for unspecified fields, such as product ID and shop ID.

### Novelty of the Idea

Unlike traditional apps that require manual entry for each transaction, our approach uses voice input to streamline the process. This reduces the burden on shopkeepers, allowing them to focus on customer service while ensuring accurate record-keeping. The final version of the solution will include notification reminders and advanced analytics to help shopkeepers manage debts and analyze sales trends effectively.

## Current Usecase for Vertex AI  Hackathon:
For this Hackathon, we are delighted to use Google's Vertex AI Agent Builder for creating agents for converting the different inputs obtained using STT models to SQL Queries.

We have used two agents, and two tools in the following way:
![image](https://github.com/bhaswata08/sqlagent/assets/74347116/68ce7ac9-7e8a-4e9d-9ce4-1613129846d4)

![image](https://github.com/bhaswata08/sqlagent/assets/74347116/daa81936-f322-45f9-a4fc-a1a6bb862d7e)

Tools:
![image](https://github.com/bhaswata08/sqlagent/assets/74347116/6300e00b-83af-4741-b8af-84eea12c5c41)
![image](https://github.com/bhaswata08/sqlagent/assets/74347116/072e62fd-fad2-4872-93d7-e809947649dc)
## Implementation Details

### How It Works

1. **Input Order Details**: The shopkeeper speaks the order details, which are captured by an STT model.
2. **Parse the Order**: The AI agent parses the text to extract relevant information such as customer name, items ordered, quantities, and prices.
3. **Generate SQL Commands**: The agent constructs SQL INSERT statements based on the extracted information.
4. **Customer ID Management**:
   - If the customer exists, retrieve their customer ID from the `customers` table.
   - If the customer is new, insert a new entry in the `customers` table and use the newly generated customer ID.
5. **Update Database**: Execute the SQL commands to update the `orders` table with the new order details.

### Example Workflow

#### Input
"Add debt for Ashish for atta 1kg ashirvaad, 5kg chawol of 300, atta was of 245, and 45 rs ka chocolate dairy milk, and 2 bidi 20 rs"

#### Generated SQL Commands
```sql
-- Check if customer exists
SELECT customer_id INTO @customer_id FROM customers WHERE customer_name = 'Ashish';

-- If customer does not exist, set a new customer_id (assuming auto-increment)
IF @customer_id IS NULL THEN
    INSERT INTO customers (customer_name) VALUES ('Ashish');
    SET @customer_id = LAST_INSERT_ID();
END IF;

-- Insert orders
INSERT INTO orders (time, product_name, price, product_id, dukaan_id, customer_id, customer_name)
VALUES (CURRENT_TIMESTAMP, 'atta 1kg ashirvaad', 245, 1, 1, @customer_id, 'Ashish'),
       (CURRENT_TIMESTAMP, 'chawol 5kg', 300, 1, 1, @customer_id, 'Ashish'),
       (CURRENT_TIMESTAMP, 'chocolate dairy milk', 45, 1, 1, @customer_id, 'Ashish'),
       (CURRENT_TIMESTAMP, 'bidi', 20, 1, 1, @customer_id, 'Ashish');
```




