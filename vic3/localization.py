from pathlib import Path

from common.localization import JominiLocalizer


class Vic3Localizer(JominiLocalizer):
    # allows the overriding of localization strings
    localizationOverrides = {'recognized': 'Recognized', # there doesn't seem to be a localization for this
                             'GNI': 'Guarani (GNI)',  # there are two tags called Guarani: GNI and GRI
                             }

    def __init__(self, game_path: Path):
        game_loc_files = sorted((game_path / 'game' / 'localization' / 'english').glob('**/*_l_english.yml'))
        mod_loc_files = sorted(Path('D:/Freddy/Documents/Paradox Interactive/Victoria 3/mod/project-utopia/localization/english').glob('**/*_l_english.yml'))
        self.localization_folder_iterator = [*game_loc_files, *mod_loc_files]