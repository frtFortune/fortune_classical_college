# Public Website Content Architecture

## Why WebsitePage exists

WebsitePage is the reusable content model for editable, page-specific public website content.

It exists so that content such as About, Admissions, FAQ, and Contact can be managed from the Django admin instead of being hardcoded in templates.

## How WebsitePage differs from SiteSettings

SiteSettings stores global website settings that apply across the whole site.

WebsitePage stores page-specific content for individual public pages.

### SiteSettings should contain
- school identity and branding
- contact details
- social links
- footer content
- default SEO defaults
- homepage-level global content
- optional global media assets

### WebsitePage should contain
- page-specific title and hero content
- page body content
- page-specific SEO fields
- publishing and ordering controls

## Future value

This separation keeps the public website maintainable and scalable.

It also creates a clean foundation for future features such as:
- richer content editing
- AI chatbot knowledge retrieval
- better SEO management
- future CMS expansion without rewriting templates

## Migration path

This simple model is intentionally lightweight. If the project later needs a richer CMS, the structure can be extended with:
- reusable content blocks
- image galleries
- page sections
- multilingual content
- draft/publish workflows

The current implementation remains simple and maintainable while preparing for those future needs.
