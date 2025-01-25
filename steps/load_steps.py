from behave import given

@given("the database is loaded with sample products")
def step_impl(context):
    context.products = [
        {"name": "Laptop", "category": "Electronics", "price": 999.99, "availability": True},
        {"name": "Shirt", "category": "Clothing", "price": 19.99, "availability": False}
    ]