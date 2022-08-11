from views import main_view, contacts_view, login_view, registration_view

routes = {
    '/': main_view,
    '/contacts': contacts_view,
    '/login': login_view,
    '/registration': registration_view
}
