% rebase('base.tpl', title=name)
<a href="/recipes" id="backbutton">
  <i class="fas fa-arrow-left"></i>
</a>
<div id="container">
  <h1>{{name}}</h1>
  <div class="flex">
    <div id="recipe">
      <p>{{description}}</p>
      <h2>Ingredienser</h2>
      <ul>
        % for item in ingredients:
          <li>{{item}}</li>
        % end
      </ul>
    </div>
    <div id="reviews">
      % for review in reviews:
        <blockquote>
          <p><q>{{review['review']}}</q></p>hgkjfdshglhgkdskjhf
          <footer>{{get('review["author"]', 'N.N')}}</footer>
          </blockquote>
      % end
      <br><br>
      <form method="post">
        <textarea name="review" placeholder="Skriv en recension"></textarea><br>
        <input type="text" name="author" placeholder="Namn"></textarea>
        <br>
        <input type="submit" value="Skicka">
      </form>
    </div>
  </div>
</div>
