<html>
    <head>
        <title>To-Do lists</title>
    </head>
    <body>
        <h1>Start a new To-Do list</h1>
        <form method="POST" action="/lists/{{ list.id }}/add_item">
            <input name="item_text" id="id_new_item" placeholder="Enter a to-do item" />
            {% csrf_token %}
            {% for item in list.item_set.all %}
                <tr><td>{{ forloop.counter }}: {{ item.text }}</td></tr>
            {% endfor %}
        </form>
    </body>
</html>
