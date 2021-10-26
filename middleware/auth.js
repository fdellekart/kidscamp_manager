export default function ({ store, route, redirect }) {
  if (route.path !== '/login') {
    if (!store.state.user) {
      return redirect('/login')
    }
  } else if (route.path === '/login') {
    if (store.state.user) {
      return redirect('/admin')
    }
  }
}
