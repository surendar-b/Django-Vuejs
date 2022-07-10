import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TreeView from '../views/treeView.vue'
import AddCategory from '../views/Addcategory.vue'
import DeleteCategory from '../views/Deletecategory.vue'
import UpdateCategory from '../views/UpdateCategory.vue'
import AddProduct from '../views/AddProduct.vue'
import DeleteProduct from '../views/DeleteProduct.vue'
import UpdateProduct from '../views/UpdateProduct.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: TreeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/treeview',
    name: 'treeview',
    component: TreeView
  },
  {
    path: '/addcategory',
    name: 'addcategory',
    component: AddCategory
  },
  {
    path: '/deletecategory',
    name: 'deletecategory',
    component: DeleteCategory
  },
  {
    path: '/updatecategory',
    name: 'updatecategory',
    component: UpdateCategory
  },
  {
    path: '/addproduct',
    name: 'addproduct',
    component: AddProduct
  },
  {
    path: '/deleteproduct',
    name: 'deleteproduct',
    component: DeleteProduct
  },
  {
    path: '/updateproduct',
    name: 'updateproduct',
    component: UpdateProduct
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
