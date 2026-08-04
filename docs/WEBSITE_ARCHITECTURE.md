# Website Architecture

## Overall Direction

The project has two distinct but connected parts:

- Public website: marketing, information, and general school communication
- Secure portal: a future authenticated area for existing students and staff

The public website is the primary product. The portal is a feature that becomes available through login once authentication is implemented.

## Public Pages

The following pages form the public website foundation:

- Home
- About
- Academics
- Admissions
- News & Events
- FAQ
- Contact
- Login

## Portal Pages

The following portal pages are planned as future authenticated areas:

- Student Portal
- Staff Portal

The portal is intentionally separate from the public marketing website so that public content can remain lightweight and content-driven while secure areas can evolve independently.

## Content Ownership

The public website should eventually pull content from the database where appropriate, including:

- School fees information
- Subjects offered
- Classes and academic stages
- News and announcements
- Contact information
- Admissions information

At the global level, the website uses a singleton SiteSettings model to power shared public content such as:

- school name and short name
- motto
- contact information
- footer text
- homepage hero content
- social media links
- default SEO metadata
- optional logo, favicon, and hero image

For page-specific public content, the project now also uses a WebsitePage model. This allows editable content for pages such as About, Admissions, FAQ, and Contact to be managed through the admin rather than hardcoded into templates.

This keeps the public site extensible and avoids hardcoded school-wide information in templates while still allowing page-specific content to be updated cleanly.

## Template-Based Content

Some content will remain layout and template driven for now, including:

- Site shell and navigation
- Basic page structure
- Global footer placeholders
- Reusable page sections and placeholders

## Future Notes

- Public-facing content should be easy to manage through the admin area later.
- Dynamic content should be introduced gradually rather than hardcoded into templates.
- Authentication, role-based access, and portal-specific functionality are out of scope for this foundation phase.
