const LIGHT_THEME = 0;
const DARK_THEME = 1;

const themesConfig = {
  0: 'light-theme',
  1: 'dark-theme',
};

function toggleTheme() {
  const toggler = document.getElementById('ThemeToggler');

  if (toggler.checked) {
    setTheme(DARK_THEME);
  } else {
    setTheme(LIGHT_THEME);
  }
}

function setTheme(theme) {
  const themeId = themesConfig[theme];
  const body = document.getElementsByTagName('body')[0];

  localStorage.setItem('theme', theme);
  body.setAttribute('data-theme', themeId);
}

const toggler = document.getElementById('ThemeToggler');
const savedTheme = parseInt(localStorage.getItem('theme'), 10);

if (savedTheme) {
  setTheme(DARK_THEME);
} else {
  setTheme(LIGHT_THEME);
}

toggler.checked = savedTheme;
toggler.addEventListener('change', () => {
  toggleTheme();
});
