import PyPDF4
import argparse

def full_page_indicies(chunk, num_pages):
    # convert chunk to 0-indexed
    chunk = [i - 1 for i in chunk]

    chunk_size = len(chunk)

    # the number of pages is a multiple of chunk_size
    new_num_pages = (num_pages + chunk_size - 1) // chunk_size * chunk_size

    new_page_indicies = []
    for i in range(new_num_pages):
        new_i = chunk[i % chunk_size] + (i // chunk_size) * chunk_size
        new_page_indicies.append(new_i)

    return new_page_indicies


def rearrange_pdf(src, dst, chunk):
    pdf_src = PyPDF4.PdfFileReader(src)
    num_pages = pdf_src.getNumPages()
    

    pdf_dst = PyPDF4.PdfFileWriter()
    for i in full_page_indicies(chunk, num_pages):
        if i < num_pages:
            pdf_dst.addPage(pdf_src.getPage(i))
        else:
            pdf_dst.addBlankPage()

    with open(dst, mode='wb') as f:
        pdf_dst.write(f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('src', type=str, help='source pdf file')
    parser.add_argument('dst', type=str, help='destination pdf file')
    parser.add_argument('indicies', nargs='+', type=int, help='page indices by which you want to order (1-indexed)')

    res = parser.parse_args()
    rearrange_pdf(res.src, res.dst, res.indicies)

if __name__ == '__main__':
    main()
