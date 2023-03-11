from ydata_profiling import ProfileReport


def get_data_profile_report(data, **kwargs):
    profile = ProfileReport(
        data,
        dark_mode=True,
        title="Data Profile Report",
        html={"navbar_show": False, "full_width": True},
        **kwargs
    )

    return profile
