% rebase('base.tpl', title=name)
<h1>{{name}}</h1>
<p>{{description}}</p>
<h2>Ingredienser</h2>
<ul>
  % for item in ingredients:
    <li>{{item}}</li>
  % end
</ul>

<br>
<br>
% for review in reviews:
  <blockquote>{{review}}</blockquote>
% end
