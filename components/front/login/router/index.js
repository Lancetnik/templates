path: '/',
component: () => import('../views/Login.vue'),
redirect: {name: 'SignIn'},
children: [
    {
      path: 'sign-in/',
      name: 'SignIn',
      component: () => import('../components/sign-in.vue'),
    },
    {
      path: 'sign-up/',
      name: 'SignUp',
      component: () => import('../components/sign-up.vue'),
    }
]