

    import pandas as pd

    def generate_car_matrix(dataset_path):
        df = pd.read_csv(dataset_path)

        car_matrix = df.pivot_table(index='id_1', columns='id_2', values='car', fill_value=0)

        car_matrix.values[[range(len(car_matrix))] * 2] = 0

        return car_matrix

    dataset_path = r'C:\Users\user\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
    result_df = generate_car_matrix(dataset_path)
    print(result_df)


    return df


def get_type_count(df)->dict:
    df = pd.read_csv(dataset_path)

    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')], labels=choices, right=False)

    type_counts = df['car_type'].value_counts().to_dict()

    sorted_type_counts = {key: type_counts[key] for key in sorted(type_counts)}

    return sorted_type_counts

    dataset_path = r'C:\Users\user\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
    result_counts = get_type_count(dataset_path)
    print(result_counts)


def get_bus_indexes(df)->list:

        df = pd.read_csv(dataset_path)


        mean_bus_value = df['bus'].mean()


        bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()


        bus_indexes.sort()

        return bus_indexes

   dataset_path = r'C:\Users\user\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
    result_indices = get_bus_indexes(dataset_path)
    print(result_indices)

    return list()





    def filter_routes(dataset_path):

        df = pd.read_csv(dataset_path)

        route_avg_truck = df.groupby('route')['truck'].mean()


        selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()


        selected_routes.sort()

        return selected_routes


    dataset_path = r'C:\Users\user\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main\datasets\dataset-1.csv'
    result_routes = filter_routes(dataset_path)
    print(result_routes)

    return list()




    def multiply_matrix(input_matrix):

        modified_matrix = input_matrix.copy(deep=True)


        modified_matrix[modified_matrix > 20] *= 0.75
        modified_matrix[modified_matrix <= 20] *= 1.25


        modified_matrix = modified_matrix.round(1)

        return modified_matrix


    result_df = generate_car_matrix('path_to_dataset.csv')
    modified_result_df = multiply_matrix(result_df)
    print(modified_result_df)


def time_check(df)->pd.Series:

        df['start_timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
        df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])

        full_day_range = pd.date_range('00:00:00', '23:59:59', freq='1S').time

        result_series = df.groupby(['id', 'id_2']).apply(lambda group: (
                group['start_timestamp'].min().time() == full_day_range[0] and
                group['end_timestamp'].max().time() == full_day_range[-1] and
                set(group['start_timestamp'].dt.dayofweek.unique()) == set(range(7))
        ))



    df = pd.read_csv('C:\Users\user\Downloads\MapUp-Data-Assessment-F-main\MapUp-Data-Assessment-F-main')
    result_series = check_timestamp_completeness(df)
    print(result_series)
    return pd.Series()
