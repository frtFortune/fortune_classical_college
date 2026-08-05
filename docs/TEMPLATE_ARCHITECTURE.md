# Public Website Template Architecture

## Purpose

The public website templates are organized around reusable include-based components so the homepage, informational public pages, and news views can evolve without duplicating markup.

## Reusable partials

The following partials are available in the `templates/includes` directory:

- `header.html`: Site header shell with branding and top actions.
- `navigation.html`: Accessible main navigation links.
- `footer.html`: Global footer text, contact details, social links, and quick links.
- `hero.html`: Homepage hero banner section.
- `page_hero.html`: Page hero header for informational public pages (About, Academics, Admissions, FAQ, Contact).
- `page_content.html`: Page body wrapper rendering database content or placeholder fallback text.
- `section_heading.html`: Section heading component with accessible aria labelling.
- `feature_card.html`: Reusable feature preview card.
- `news_card.html`: Reusable news item card component supporting custom heading levels, publication dates, and detail links.
- `call_to_action.html`: Reusable Call-to-Action banner component.

## Page Usage

- **Informational Pages (`about.html`, `academics.html`, `admissions.html`, `faq.html`, `contact.html`)**:
  Extend `base.html` and utilize `page_hero.html` and `page_content.html` to eliminate duplicated hero and body placeholder markup.
- **News List (`news/list.html`)**:
  Uses `news_card.html` for rendering featured and general news announcements.
- **Homepage (`home.html`)**:
  Uses `hero.html`, `section_heading.html`, `feature_card.html`, and `call_to_action.html`.

## Design goals

- Keep the public website as the primary product.
- Keep the portal separate and untouched by the public template architecture.
- Use semantic HTML5 structure and accessible navigation.
- Maintain the current placeholder policy.
- Prepare templates for future data from `SiteSettings`, `WebsitePage`, `NewsItem`, and academic models.

## Future extension path

The current structure is intentionally lightweight. As the project grows, these partials can be extended or styled without rewriting page-level template shells or duplicating HTML structures.

