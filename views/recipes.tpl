% rebase('base.tpl', title="Drinkrecept")
<a href="/" id="backbutton">
  <i class="fas fa-arrow-left"></i>
</a>
<div id="container">
  <h1>Drinkar</h1>
  % for recipe in recipes:
      <a href="{{recipe["link"]}}" class="recipe-link">{{recipe["name"]}}</a><br>
  % end
  <br>
  <a href="/create/recipe">+ Skapa nytt recept +</a>
</div>
