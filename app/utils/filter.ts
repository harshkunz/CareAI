export function filterMedicalResponse(raw: string): string {
  if (!raw) return "<p>No information available.</p>";

  // Split response into paragraph + bullet points
  const parts = raw.split("•");
  const paragraph = parts[0].trim();
  const bullets = parts.slice(1).map(p => p.trim()).filter(Boolean);

  // Format into HTML
  let html = `<p class="text-gray-200 leading-relaxed mb-3">${paragraph}</p>`;

  if (bullets.length > 0) {
    html += `<ul class="list-disc list-inside text-gray-300 space-y-1">`;
    bullets.forEach(point => {
      html += `<li>${point}</li>`;
    });
    html += `</ul>`;
  }

  return html;
}