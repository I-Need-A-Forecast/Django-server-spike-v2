# Building various views and calls that are expected.

#The first DB parser we built.
def wx_passer(request, station_id, obsdate):
    response = {"data": [],
    "param": station_id}
    query = CurrentObservation.objects.all()
    query = query.filter(
        obsdate = obsdate,
        station_id = station_id
    )

    for result in query:
        response["data"].append({
            "obstime": result.obstime,
            "temp_f": result.temp_f,
            "temp_c": result.temp_c
        })

    return JsonResponse(response)

### This one attempts to pull in the latest five (5) readings from a specific site.
def get_WxObservation(request, get_StationId, get_Obsdate, get_Obstime):
    WxObservations = {
        "Reporting Station": get_StationId,
        "Observation Date": get_Obsdate,
        "Observation Time": get_Obstime,
        "Observed Weather": []
    }
    query = CurrentObservation.objects.all()
    query = query.order_by(
        '-obsdate',
        '-obstime'
    ).filter(
        station_id = get_StationId
    )