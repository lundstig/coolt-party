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
          % if "rating" in review and review["rating"]:
            <p>
              % for i in range(review["rating"]):
                ★
              % end
              % for i in range(5 - review["rating"]):
                ☆
              % end
            </p>
          % end
          <p><q>{{review['review']}}</q></p>
          <footer>{{review["author"] or "Okänd"}}</footer>
          </blockquote>
      % end
      <br><br>
      <form method="post">
        <select name="rating">
          <option>1/5</option>
          <option>2/5</option>
          <option>3/5</option>
          <option>4/5</option>
          <option>5/5</option>
        </select><br>
        <textarea name="review" placeholder="Skriv en recension"></textarea><br>
        <input type="text" name="author" placeholder="Namn">
        <br>
        <input type="submit" value="Skicka">
      </form>
    </div>
  </div>
</div>
