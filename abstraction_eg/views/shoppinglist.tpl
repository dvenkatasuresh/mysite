<html>
<body>
<h2>Shopping List</h2>
<hr/>
<table>
% for item in shopping_list:
  <tr>
    <td>{{str(item['desc'])}}</td>
    <td><a href="/edit/{{str(item['id'])}}">edit</a></td>
    <td><a href="/delete/{{str(item['id'])}}">delete</a></td>
  </tr>
% end
</table>
<hr/>
<a href="/add">Add new item...</a>
</body>
</html>