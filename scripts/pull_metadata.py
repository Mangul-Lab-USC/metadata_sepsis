import pandas as pd
import xmltodict
import os


def parse_xml(filepath):
    with open(filepath) as fd:
        data_dict = xmltodict.parse(fd.read())

    accession = filepath.split('/')[-1].split('_')[0]
    print(accession)
    print('\n')
    r_df = pd.DataFrame()

    for sample in data_dict['MINiML']['Sample']:
        tmp_df = {}

        if 'Status' in sample:
            tmp_df['database'] = [sample['Status']['@database']]
            tmp_df['submission_date'] = [sample['Status']['Submission-Date']]
            tmp_df['release_date'] = [sample['Status']['Release-Date']]
            tmp_df['last_update_date'] = [sample['Status']['Last-Update-Date']]
        tmp_df['title'] = [sample['Title']]
        tmp_df['accession'] = [sample['Accession']['#text']]
        tmp_df['type'] = [sample['Type']]
        tmp_df['source'] = [sample['Channel']['Source']]
        tmp_df['organism'] = [sample['Channel']['Organism']['#text']]

        if isinstance(sample['Channel']['Characteristics'], list):
            count = 0
            for c in sample['Channel']['Characteristics']:
                if '@tag' in c:
                    if '#text' in c:
                        tmp_df[c['@tag']] = [c['#text']]
                    else:
                        tmp_df[c['@tag']] = ['']
                else:
                    tmp_df['characteristic_' + str(count)] = [c]
                count += 1
        elif isinstance(sample['Channel']['Characteristics'], dict):
            if '@tag' in sample['Channel']['Characteristics']:
                tmp_df[sample['Channel']['Characteristics']['@tag']] = [sample['Channel']['Characteristics']['#text']]
            else:
                tmp_df['characteristic'] = [sample['Channel']['Characteristics']]
        else:
            tmp_df['characteristic'] = [sample['Channel']['Characteristics']]

        if 'Treatment-Protocol' in sample['Channel']:
            tmp_df['treatment_protocol'] = [sample['Channel']['Treatment-Protocol']]
        tmp_df['molecule'] = [sample['Channel']['Molecule']]
        if 'Extract-Protocol' in sample['Channel']:
            tmp_df['extract_protocol'] = [sample['Channel']['Extract-Protocol']]
        if 'Label' in sample['Channel']:
            tmp_df['label'] = [sample['Channel']['Label']]
        if 'Label-Protocol' in sample['Channel']:
            tmp_df['label_protocol'] = [sample['Channel']['Label-Protocol']]
        if 'Hybridization-Protocol' in sample:
            tmp_df['hybridization_protocol'] = [sample['Hybridization-Protocol']]
        if 'Scan-Protocol' in sample:
            tmp_df['scan_protocol'] = [sample['Scan-Protocol']]
        if 'Description' in sample:
            tmp_df['description'] = [sample['Description']]
        if 'Data-Processing' in sample:
            tmp_df['data_processing'] = [sample['Data-Processing']]
        r_df = r_df.append(pd.DataFrame.from_dict(tmp_df), ignore_index=True, sort=False)
    if os.path.exists('../summary_data'):
        r_df.to_csv('../summary_data/' + accession + '_metadata.csv', index=False)
    else:
        os.mkdir('../summary_data')
        r_df.to_csv('../summary_data/' + accession + '_metadata.csv', index=False)


if __name__ == '__main__':
    for file in os.listdir('../raw_data'):
        parse_xml('../raw_data/' + file)
