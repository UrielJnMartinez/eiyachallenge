
const url = 'http://0.0.0.0:8000/fleet_admin/'
import CitiesList from '../components/CitiesList.js'
import VehiclesList from '../components/VehiclesList.js'
Vue.createApp({
    data() {
        return { 
            items: []
        }
      },
    
    components: {
        "cities-list":CitiesList,
        "vehicles-list":VehiclesList
    },
    methods:{
        listCity(){
            axios.get(`${url}cities/`).then((response)=> {
                console.log(response.data)
                this.items = response.data
            }).catch(error => console.log(error))
        },
        addCity(){
            console.log('new city')
        }
    },
    created(){
        this.listCity();
    }
  }).mount('#app')
