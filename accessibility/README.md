# A Crash Course on Accessibility

This README provides an overview of accessibility concepts and resources to help make digital content accessible to all users, including those with disabilities.

## WCAG Timeline

- 1999: WCAG 1.0 released by W3C
- 2008: WCAG 2.0 (current version) released
- 2012: WCAG 2.0 became ISO standard
- 2017: WCAG 2.1 draft under public review
- 2018: WCAG 2.1 became ISO standard
- 2020: WCAG 2.2 working draft and WCAG 3.0 (called "Silver") is also in the working phase

## Four Principles (POUR)

1. **Perceivable**: Can users perceive the content? Consider different senses and ensure content is accessible to all users.
2. **Operable**: Can users use UI components and navigate the content? Ensure operability for users with different abilities.
3. **Understandable**: Can users understand the content? Provide clear and consistent interfaces to avoid confusion.
4. **Robust**: Can the content be consumed by a wide variety of user agents (browsers)? Ensure compatibility with assistive technologies and different user agents.

## Accessibility Levels

WCAG defines three levels of accessibility:

- **Level A (required)**: Improves basic accessibility by enhancing site navigation and content translation.
- **Level AA (required)**: Makes content accessible to a wider range of disabilities, including color contrast and error identification.
- **Level AAA (optional)**: The highest level of accessibility compliance, recommended but not required due to potential design impact.

## Resources

- [Accessibility Conformance Levels: Standards](https://www.w3.org/WAI/WCAG21/quickref/?currentsidebar=%23col_overview&levels=a%2Caa%2Caaa)
- ARIA (Accessible Rich Internet Applications)
- A11y testing tools
- Companies dedicated to A11y

## ARIA (Accessible Rich Internet Applications)

- ARIA provides extra information to assistive technologies (e.g., screen readers) via attributes added to HTML.
- Use native HTML elements whenever possible and avoid using ARIA as a quick-fix.

## A11y Testing Tools

Differentiate between automated and manual tools:

- Automated tools: Axe, Lighthouse, etc. (around 49% of tests)
- Manual tools: Screen readers, code analysis, etc. (around 55% of tests)

Companies dedicated to A11y: Siteimprove, Tenon.io, Deque, The Paciello Group, etc.

## Screen Readers

- Examples: VoiceOver (Apple products), JAWS (expensive), NVDA (open-source alternative)
- Enable VoiceOver on Mac OSX: Preferences -> Accessibility -> VoiceOver
- Basic shortcuts for VoiceOver (Mac OSX)

## Keyboard Navigation

- Some users rely on keyboard navigation instead of a mouse.
- Test pages using only the keyboard to ensure accessibility.

## Skip Links

- Facilitate keyboard navigation by allowing users to skip directly to important sections of a page.
- Bypass Blocks: Provide a mechanism to skip repeated content on multiple web pages.

For more information and detailed resources on accessibility, please refer to the relevant links provided in each section.

**Note**: This README provides an overview and references for accessibility. Please consult the linked resources for more in-depth guidance on specific topics.
