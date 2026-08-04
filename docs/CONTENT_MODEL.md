# Website Content Model

## Site-wide public content

The global website content is managed through the SiteSettings singleton model.

This model provides the shared values used across the public website, including:

- school identity and branding
- contact details
- homepage hero content
- footer content
- social links
- default SEO metadata
- optional logo, favicon, and hero image assets

## Content ownership

The following website information should come from SiteSettings:

- School name
- Short name
- Motto
- Primary and secondary phone numbers
- Primary email address
- Address
- Office hours
- Homepage hero title and subtitle
- Footer text
- Social media URLs
- Default meta description
- Optional logo, favicon, and hero image

## Notes

- SiteSettings is a singleton, so there should only ever be one record.
- The model is intentionally general so that future public website pages can reuse the same global content without hardcoded values.
- Templates receive SiteSettings automatically through the context processor, so they do not need to query the database directly.
