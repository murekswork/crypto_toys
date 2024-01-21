function ajaxSelectCoin(coin_name) {
    var currency = document.getElementById('currency').value
    $.ajax({
        url: URL_SEND_COIN,
        method: 'post',
        data: {
            'currency': currency,
            'coin_name': coin_name,
            'csrfmiddlewaretoken': TOKEN
        },
        success: function (data) {
            let coin_data = data.coin
            console.log(data)
            var output_cont = document.getElementById('output-data-container')
            output_cont.innerHTML = ''
            for (var key in coin_data) {
                output_cont.innerHTML += `<p class="small">${key}: ${coin_data[key]}</p>`
            }
        }
    })
}

let selected_currency = 'rub'

let updateDataPeriodicFunction = setInterval(function () {
    ajaxGetFullData(selected_currency)
}, 80000)

document.addEventListener('DOMContentLoaded', function () {
    ajaxGetFullData(selected_currency)
})

function ajaxGetFullData(currency) {
    selected_currency = currency
    $.ajax({
            url: URL_GET_FULL_DATA,
            method: 'post',
            data:
                {
                'csrfmiddlewaretoken': TOKEN,
                'currency': currency
                },
            success: function (full_data) {
                let table = document.getElementById('coins-table-body')
                let i = 1
                table.innerHTML = null
                for (let key in full_data) {
                    for (let ccc in full_data[key]) {
                        table.innerHTML +=

                            `<th>${i}</th>
                            <td>${full_data[key][ccc]['id']}</td>
                            <td>${full_data[key][ccc]['current_price']} ${currency}</td>
                            <td>${full_data[key][ccc]['market_cap']} ${currency}</td>
                            <td>${full_data[key][ccc]['total_volume']}</td>
                            <td class="percentage">${full_data[key][ccc]['price_change_percentage_1h_in_currency']}%</td>
                            <td class="percentage">${full_data[key][ccc]['price_change_percentage_24h_in_currency']}%</td>
                            <td class="percentage">${full_data[key][ccc]['price_change_percentage_7d_in_currency']}%</td>`
                    i = i + 1
                    let tds = document.getElementsByClassName('percentage')
                    console.log(tds)
                    for (let td of tds) {
                        if (parseFloat(td.innerText) < 0) {
                            td.className = 'table-danger';
                        }
                        else
                        {
                            td.className = 'table-success';
                        }
                    }
                    }


                }

            }



        }
    )

}


