<html>
    <head>
        <title>To-Do lists</title>
    </head>
    <body>
        <h1>Start a new To-Do list</h1>
        <form method="POST">
            <input name="item_text" id="id_new_item" placeholder="Enter a to-do item" />
            {% csrf_token %}
        </form>
    </body>
</html>
