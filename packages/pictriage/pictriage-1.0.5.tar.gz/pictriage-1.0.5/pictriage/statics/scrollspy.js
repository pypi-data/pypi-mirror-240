let sections = document.querySelectorAll('.folder');
let currentSectionIndex = 0;
window.addEventListener("scroll", () => {
  const sectionMargin = 200;
  currentSectionIndex = sections.length - [...sections].reverse().findIndex((section) => window.scrollY >= section.offsetTop - sectionMargin) - 1
});

function jumpSection(n) {
  let newIndex = currentSectionIndex + n;
  if (newIndex < 0 || newIndex >= sections.length) return;
  sections[newIndex].scrollIntoView();
}
