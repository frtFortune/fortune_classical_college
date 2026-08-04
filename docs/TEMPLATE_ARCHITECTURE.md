# Public Website Template Architecture

## Purpose

The public website templates are now organized around reusable include-based components so the homepage and other public pages can evolve without duplicating markup.

## Reusable partials

The following partials are available in the templates/includes directory:

- header.html
- navigation.html
- footer.html
- hero.html
- section_heading.html
- feature_card.html
- news_card.html
- call_to_action.html

These components provide the foundation for a scalable public website layout while remaining simple and maintainable.

## Design goals

- Keep the public website as the primary product.
- Keep the portal separate and untouched by the public template architecture.
- Use semantic HTML5 structure and accessible navigation.
- Use placeholders until real content is available.
- Prepare templates for future data from SiteSettings, WebsitePage, News, Announcements, and academic models.

## Future extension path

The current structure is intentionally lightweight. As the project grows, these partials can be extended or replaced with richer data-driven components without rewriting the whole site shell.
