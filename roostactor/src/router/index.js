import { createRouter, createWebHistory } from "vue-router";
import Login from "@/views/Login.vue";
import Dashboard from "@/views/Dashboard.vue";
import Korisnici from "@/views/Korisnici.vue";
import Projekti from "@/views/Projekti.vue";
import Uloge from "@/views/Uloge.vue";
import RasporedSnimanja from "@/views/RasporedSnimanja.vue";
import Statistika from "@/views/Statistika.vue";
import Obavestenja from "@/views/Obavestenja.vue";
import KorisnikNovi from "@/views/KorisnikNovi.vue";
import ProjekatNovi from "@/views/ProjekatNovi.vue";
import UlogaNovi from "@/views/UlogaNovi.vue";
import KorisnikIzmena from "@/views/KorisnikIzmena.vue";
import IzmeniProfil from "@/views/IzmeniProfil.vue";
import ProjekatIzmena from "@/views/ProjekatIzmena.vue";
import ProjekatInfo from "@/views/ProjekatInfo.vue";
import InfoIzmena from "@/views/InfoIzmena.vue";
import StatistikaIzmena from "@/views/StatistikaIzmena.vue"


const routes = [
{
path: "/login",
name: "Login",
component: Login,
},
{
path: "/dashboard/:id",
name: "dashboard",
component: Dashboard,
props:true,
},
{
path: "/korisnici",
name: "korisnici",
component: Korisnici,
},
{
path: "/projekti",
name: "projekti",
component: Projekti,
},
{
    path: "/uloge",
    name: "uloge",
    component: Uloge,
    },
{
    path: "/raspored",
    name: "raspored-snimanja",
    component: RasporedSnimanja,
    },
{
    path: "/statistika",
    name: "statistika",
    component: Statistika,
    meta: { requiresRole: ["Administrator"] },
    },
{
    path: "/obavestenja",
    name: "obavestenja",
    component: Obavestenja,
    },
    {
        path: "/korisnik-novi",
        name: "korisnik-novi",
        component: KorisnikNovi, 
        meta: { requiresRole: ["Administrator"] },
      },
      {
        path: "/projekat-novi",
        name: "projekat-novi",
        component: ProjekatNovi, 
        meta: { requiresRole: ["Administrator"] },
      },
      {
        path: "/uloga-novi",
        name: "uloga-novi",
        component: UlogaNovi, 
      },
      { 
        path: "/korisnik-izmena/:id", 
        name: "KorisnikIzmena", 
        component: KorisnikIzmena, 
        props: true, 
        meta: { requiresRole: ["Administrator"] },
      },
      {
        path: "/profil-izmena/:id", 
        name: "IzmeniProfil", 
        component: IzmeniProfil, 
        props: true, 
      },
      {
        path: "/projekat-izmena/:id", 
        name: "ProjekatIzmena", 
        component: ProjekatIzmena, 
        props: true, 
        meta: { requiresRole: ["Administrator"] },
      },
      {
        path: "/projekat-info/:id", 
        name: "ProjekatInfo", 
        component: ProjekatInfo, 
        props: true, 
      },
      {
        path: "/info-izmena/:id", 
        name: "InfoIzmena", 
        component: InfoIzmena, 
        props: true, 
        meta: { requiresRole: ["Administrator"] },
      },
      {
        path: "/statistika-izmena/:id", 
        name: "StatistikaIzmena", 
        component: StatistikaIzmena, 
        props: true, 
        meta: { requiresRole: ["Administrator"] },
      }

      
];
const router = createRouter({ 
    history: createWebHistory(import.meta.env.BASE_URL), 
    routes, 
  }); 

  router.beforeEach((to, from, next) => {
    const role = localStorage.getItem("rola");
    console.log("Role from localStorage:", role);
  
    if (role) {
      if (to.meta.requiresRole && !to.meta.requiresRole.includes(role)) {
        console.log("Redirecting to login due to insufficient role");
        return next("/login");
      }
    } else if (to.meta.requiresRole) {
      console.log("Redirecting to login because no role found");
      return next("/login");
    }
  
    next();
  });
  

export default router;
