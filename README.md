# 📚 CS50W Wiki — Django Encyclopedia Project

A Wikipedia-style online encyclopedia built using **Django**, based on the requirements of **CS50 Web Programming (Project 1)**.  
Users can view, search, create, edit, and browse random encyclopedia entries stored in Markdown format.

[![Watch the demo on YouTube](https://img.youtube.com/vi/tXZhEg8xM5s/0.jpg)](https://youtu.be/tXZhEg8xM5s)  
*Click the image above to watch the demo video.*

---

## ⭐ Features

### ✔ View Entry (`/<title>`)
- Displays the content of an encyclopedia entry.  
- Markdown is converted to HTML using **markdown2**.  
- If the entry does not exist, a custom **not_found** page is shown.

---

### ✔ Search (`/search/`)
- If the search query **exactly matches** an entry (case-insensitive), the user is redirected to that entry.  
- Otherwise, a **search results** page shows all entries containing the query as a substring.  
- If no matches exist, user is shown the `not_found` page.

---

### ✔ Create New Page (`/new_page/`)
- Uses a Django `Form` (`NewPageForm`) with fields:  
  - `title`  
  - `body` (Markdown)  
- Prevents duplicate page titles.  
- On success, saves new entry using `util.save_entry()` and redirects to the page.

---

### ✔ Edit Entry (`/<title>/edit`)
- Pre-populated form (same form as creation).  
- Allows the user to edit Markdown contents of any entry.  
- Saving updates the Markdown file and redirects to the entry.

---

### ✔ Random Page (`/random/`)
- Redirects the user to a randomly selected entry.

---

## 🗂 URL Structure

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("random/", views.random_page, name="random_page"),
    path("search/", views.search, name="search"),
    path("new_page/", views.new_page, name="new_page"),
    path("<str:title>", views.entry, name="entry"),
    path("<str:title>/edit", views.edit, name="edit"),
]
