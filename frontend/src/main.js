import { createApp } from 'vue'
import {createRouter, createWebHistory} from "vue-router";
import App from './App.vue'
import Header from './components/Header.vue'
import Rockets from './components/Rockets.vue'
import Launches from './components/Launches.vue'
import Home from './components/Home.vue'
import Starlink from './components/Starlink.vue'
import Spinner from './components/Spinner.vue'
import Alert from './components/Alert.vue'
import ScatterPlot from './components/ScatterPlot.vue'
import AreaChart from './components/AreaChart.vue'
import CircularPlot from './components/CircularPlot.vue'



const router = createRouter({
    history: createWebHistory(),
    routes:[
        {path: '/', component: Home},
        {path: '/rockets', component: Rockets},
        {path: '/launches', component: Launches},
        {path: '/starlink', component: Starlink},
    ],
    linkActiveClass:'active'
});

const app = createApp(App)

app.use(router)

app.component('Header', Header);
app.component('Home', Home);
app.component('Rockets', Rockets);
app.component('Launches', Launches);
app.component('Starlink', Starlink);
app.component('Spinner', Spinner);
app.component('Alert', Alert);
app.component('ScatterPlot', ScatterPlot);
app.component('AreaChart', AreaChart);
app.component('CircularPlot', CircularPlot);



app.mount('#app')
