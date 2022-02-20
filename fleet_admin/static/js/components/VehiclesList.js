const url = 'http://0.0.0.0:8000/fleet_admin/'

export default{
    props : {
        items_list : {
            type: Array,
            required:true,
            default:'No hay vehiculos en esta ciudad'
        },
        cities_list : {
            type: Array,
            required:true,
            default:'No hay mas ciudades'
        }
    },
    methods :{
        changeCity: function(event,city_origin,vehicle_id) {
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

            axios({
                method:  'put',
                url:`${url}vehicles/detail/${vehicle_id}/`,
                data: {
                    id:vehicle_id,
                    current_location:event,
                }
            })

            .then((respose) => {
                if (respose.data.status==200){
                    console.log('succes')
                }
            }).catch((err) => {
                console.log(err)
            });
        },
        
    },
    template:
    `
    <table class="table">
        <thead>
            <tr>
            <th scope="col">Combustible consumido</th>
            <th scope="col">Distancia recorrida</th>
            <th scope="col">Km/l </th>
            <th scope="col">Enviar a</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(item,idx) in items_list" :key="idx">
                <td>{{item.spent_fuel}}</td>
                <td>{{item.distance_covered}}</td>
                <td>{{item.fuel_usage_km}}</td>
                <td>
                <select class="form-select" aria-label="seleccionar ciudad" 
                    @change="changeCity($event.target.value,item.current_location.id,item.id)">
                    <option 
                        v-for="(city,idx) in cities_list"
                        v-bind:value=city.id
                        :selected="option == item.current_location.name">
                        {{city.name}}
                    </option>
                    
                </select>
                </td>

            </tr>
        </tbody>
        </table>
    `
}