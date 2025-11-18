def split_csv_line(line):
    fields = []
    cur = ""
    in_quotes = False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == '"':
            if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                cur += '"'
                i += 1
            else:
                in_quotes = not in_quotes
        elif ch == ',' and not in_quotes:
            fields.append(cur)
            cur = ""
        else:
            cur += ch
        i += 1
    fields.append(cur)
    return fields

def sort_songs_by_release(input_csv_path, output_csv_path):
    with open(input_csv_path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    if not lines:
        return tuple()

    header = split_csv_line(lines[0])
    # normalize header names: strip, remove BOM if present, lowercase
    normalized = [h.strip().lstrip('\ufeff').lower() for h in header]

    try:
        idx_name = normalized.index('track_name')
        idx_date = normalized.index('album_release_date')
    except ValueError:
        # helpful debug message showing what the parser actually read
        raise ValueError(
            "Input CSV must contain 'track_name' and 'album_release_date' headers. "
            "Found headers: " + ", ".join(f"'{h}'" for h in normalized)
        )

    entries = []
    for line in lines[1:]:
        if not line.strip():
            continue
        fields = split_csv_line(line)
        # skip malformed rows
        if idx_name >= len(fields) or idx_date >= len(fields):
            continue
        name = fields[idx_name]
        date = fields[idx_date] or '0000-00-00'
        entries.append((date, name))

    # sort by date string (YYYY-MM-DD sorts lexicographically)
    entries.sort(key=lambda pair: pair[0])

    sorted_names_tuple = tuple(name for date, name in entries)

    def escape_field(field):
        if '"' in field:
            field = field.replace('"', '""')
        if ',' in field or '"' in field or '\n' in field:
            return '"' + field + '"'
        return field

    with open(output_csv_path, 'w', encoding='utf-8', newline='') as out:
        out.write('track_name,album_release_date\n')
        for date, name in entries:
            out.write(f"{escape_field(name)},{escape_field(date)}\n")

    return sorted_names_tuple

if __name__ == '__main__':
    input_csv = r'c:\Users\jinas\Downloads\taylor_discography.csv'
    output_csv = r'c:\Users\jinas\Downloads\sorted_tracks_by_release.csv'
    sorted_tuple = sort_songs_by_release(input_csv, output_csv)
    print('Wrote', output_csv)
    print('Total tracks written:', len(sorted_tuple))
    print('First 10 tracks (oldest→newest):')
    for track in sorted_tuple[:10]:
        print(track)