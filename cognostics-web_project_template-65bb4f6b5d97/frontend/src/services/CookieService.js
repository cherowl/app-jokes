export default class CookieService {
  static setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = date.toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/`;
  }

  static getCookie(name) {
    const searchName = `${name}=`;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i];
      while (cookie.charAt(0) === ' ') {
        cookie = cookie.substring(1);
      }
      if (cookie.indexOf(searchName) === 0) {
        return cookie.substring(searchName.length, cookie.length);
      }
    }
    return '';
  }

  static deleteCookie(name) {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
  }

  static cookieIsSet(name) {
    const cookie = CookieService.getCookie(name);
    return cookie !== '';
  }
}
