from behave import when, then

@when("I send a GET request to \"/products\"")
def step_impl(context):
    context.response = context.client.get("/products")

@then("I should receive a list of all products")
def step_impl(context):
    assert context.response.status_code == 200

@when("I send a GET request to \"/products?name=Laptop\"")
def step_impl(context):
    context.response = context.client.get("/products?name=Laptop")

@then("I should receive the product with name \"Laptop\"")
def step_impl(context):
    assert context.response.status_code == 200
    assert "Laptop" in context.response.json["name"]