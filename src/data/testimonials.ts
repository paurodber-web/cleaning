export interface Testimonial {
  quote: string;
  customer: string;
  detail: string;
  source: string;
  rating: number;
}

/**
 * Shared testimonial bank for suburb landing pages.
 *
 * Replace or extend these entries with the approved customer testimonials.
 * The suburb template selects three entries from this bank based on its slug,
 * so reviews rotate automatically without being duplicated in every Markdown file.
 */
export const testimonials: Testimonial[] = [
  {
    quote: 'Everything felt fresh without that strong chemical smell. Booking was easy, communication was clear and the attention to our kitchen was excellent.',
    customer: 'Verified customer',
    detail: 'Regular clean',
    source: 'Google',
    rating: 5,
  },
  {
    quote: 'They made the final week of our move so much easier. The apartment looked ready for inspection and we could focus on settling into the new place.',
    customer: 'Verified customer',
    detail: 'End of lease clean',
    source: 'Google',
    rating: 5,
  },
  {
    quote: 'Reliable, lovely to deal with and consistently thorough. Having the same regular rhythm has genuinely given us part of our weekend back.',
    customer: 'Verified customer',
    detail: 'Fortnightly clean',
    source: 'Google',
    rating: 5,
  },
];

export function getTestimonialsForSuburb(slug: string, count = 3): Testimonial[] {
  if (testimonials.length === 0 || count <= 0) return [];

  const start = Array.from(slug).reduce(
    (total, character) => total + character.codePointAt(0)!,
    0,
  ) % testimonials.length;

  return Array.from(
    { length: Math.min(count, testimonials.length) },
    (_, index) => testimonials[(start + index) % testimonials.length],
  );
}
