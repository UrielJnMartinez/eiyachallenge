import VehiclesList from "./VehiclesList.js"
const url = 'http://0.0.0.0:8000/fleet_admin/'
export default {

    props : {
        items_list : {
            type: Array,
            required:true,
            default:'No hay ciudades para mostrar'
        }
    },
    components :{
        VehiclesList,
    },
    methods :{
        addNewCity(name,event) {
            console.log(name)
        },
        
    },
    template:
    `
    <div class="container">
        <div class="container-sm" v-for="(item,idx) in items_list" :key="idx" >
            <div class="card mb-4 rounded-3 shadow-sm">
                <div class="card-header py-3">
                    <h4 class="my-0 fw-normal">{{item.name}}</h4>
                </div>
                <div class="card-body">
                    
                    <vehicles-list :items_list="item.vehicle"></vehicles-list>
                    <button type="button" class="w-100 btn btn-lg btn-outline-primary">Agregar un vehiculo</button>
                </div>
            </div>
        </div>
    </div>
    
    `
}