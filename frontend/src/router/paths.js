/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
export default [
      {
    path: '/login',
     name: 'login Page',
    view: 'Login',
  },
  {
    path: "/view-audio",
    name: 'ViewAudioSet',
    view: 'ViewAudioSet'
  },
  {
    path: '',
    // Relative to /src/views
    view: 'Dashboard',
        meta: {
      requiresAuth: true
    }

  },
  {
    path: '/user-profile',
    name: 'User Profile',
        meta: {
      requiresAuth: true
    },
    view: 'UserProfile'
  },
    {
    path: '/audio-set',
    name: 'Manage Audio Set',
    view: 'AudioSet',
  },
  {
    path: '/add-audio-set',
    name: 'Add Audio Set',
        meta: {
      requiresAuth: true
    },
    view: 'AddAudioSet',
  },
  {
    path: '/table-list',
    name: 'Table List',
    meta: {
      requiresAuth: true
    },
    view: 'TableList'
  },
  {
    path: '/typography',
    view: 'Typography'
  },
  {
    path: '/icons',
    view: 'Icons'
  },
  {
    path: '/maps',
    view: 'Maps'
  },
  {
    path: '/notifications',
    view: 'Notifications'
  },
  {
    path: '/upgrade',
    name: 'Upgrade to PRO',
    view: 'Upgrade'
  }
]
