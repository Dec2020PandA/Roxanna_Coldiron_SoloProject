Roxanna Coldiron - Solo Project Proposal
========================================

Summary Paragraph:
------------------

My project will be a generic quoting tool for a business website, where the user can select products and then receive a quote for them, similar to an e-commerce experience. Superusers will be able to add new products or services in the Django admin. When a customer requests a quote from a product/service page, the product/service choice will be pre-selected for them on the quote request form.

Features List:
--------------

**P0** - Django Admin, images, Django Forms, Django built-in User and Authentication

Models
- Blogs or Posts
- Products and/or Services (title, images, description)

**P1** - Templates, Bootstrap CSS

Templates
- Base.html, to be extended by the other templates
- Product or Service page
- Front page
- Blog posts page
- Request A Quote form page

CHANGES FROM ORIGINAL PROPOSAL:
===============================
- The backend took a while so I ended up not using sass this time.
- I learned about the built-in Django auth system and used it with very little customization for this round. I wanted to get familiar with how it worked.
- I learned a lot about using Django form classes. For the next round, I may need to convert the Quote form into a model form to be able to save its data to the database and show up in admin.
- However, I did end up incorporating an API! The TinyMCE editor is used in models accessed in the admin. [Tiny MCE] (https://www.tiny.cloud) as well as a package that creates a Rich Text Field.
- I ended up working with several apps in this project but want to reorganize so that these are in an apps folder in the next round. 
- I also want to refactor and upgrade to Django 3.0 when I work some more on this.
- Images can be uploaded but not sure why they won't display. I think it has something to do with the fact it's not a real server so I tried updating some settings to allow for media to show in localhost and DEBUG mode but so far, it hasn't worked. Images in the src folder work fine.

**P3** - Enhancements

New features
- Quote Form data added to the admin with option to download as CSV
- Email backend for Quote Form
- Turn the quote cart and add-to-quote tool into a standalone Python/Django package
- Users can leave reviews that admin must approve before they publish

What's new to me 
----------------
- Django Admin
- Django User and Authentication (built-in)
- Django Forms (forms.py)
- Tiny MCE API
- Multiple apps