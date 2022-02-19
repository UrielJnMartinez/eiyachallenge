export default{
    props : {
        items_list : {
            type: Array,
            required:true,
            default:'No hay vehiculos en esta ciudad'
        }
    },
    methods :{
        changeCity(city_id,event) {
            console.log(city_id)
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
                <select class="form-select" aria-label="Default select example">
                    <option selected>Open this select menu</option>
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                </select>
                </td>

            </tr>
        </tbody>
        </table>
    `
}