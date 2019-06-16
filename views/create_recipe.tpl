% rebase('base.tpl')
<a href="/recipes" id="backbutton">
  <i class="fas fa-arrow-left"></i>
</a>
<div id="container">
  <h2>Nytt recept</h2>
  <form method="post">
    <label for="name">Namn:</label><br>
    <input name="name" type="text"><br>

    <label for="description">Beskrivning:</label><br>
    <textarea name="description"></textarea><br>

    <label for="ingredients">Ingredienser, 1 per rad:</label><br>
    <textarea name="ingredients"></textarea><br>

    <br>
    <input type="submit" value="Skapa recept">
  </form>
  % if defined('errors'):
    <br>
    <p>{{errors}}</p>
  % end
</div>
