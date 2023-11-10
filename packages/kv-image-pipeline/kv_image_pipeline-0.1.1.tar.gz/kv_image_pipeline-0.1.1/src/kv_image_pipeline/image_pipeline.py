import os.path

from kv_pdf_processor import pdf_splitter, pdf_to_image
from kv_segmentor import segmentor


class ImagePipeline:

    def __init__(self,
                 pdf_path: str = "",
                 output_dir_path: str = "",
                 file_name: str = ""
                 ):
        self.pdf_path=pdf_path
        self.output_dir_path=output_dir_path
        self.file_name=file_name

    def split_pages(self)  -> None:
        """
        This function splits a multi-page pdf into single page pdfs
        :return: None
        """

        # Check to see if the output directory path exists
        if not os.path.exists(self.output_dir_path):
            os.makedirs(self.output_dir_path)

        pdf_splitter.split_pdf(file_path=self.pdf_path,
                               file_base_name=self.file_name,
                               output_dir=self.output_dir_path)

    def convert_pdfs_to_images(self) -> None:
        """

        :return:
        """

        for file in os.listdir(self.output_dir_path):
            print(file)
            if file.endswith('.pdf'):
                pdf_to_image.convert_pdf_to_jpeg(pdf_path=self.output_dir_path+'/'+ file,
                                                 output_dir=self.output_dir_path+'/images',
                                                 dpi=300)

    def segment_images(self) -> None:
        """

        :return:
        """
        print(self.output_dir_path + '/images')
        for file in os.listdir(self.output_dir_path + '/images'):
            print(file)
            if file.endswith('.jpeg'):

                seg = segmentor.Segmentor(model_path="test/best_segmentation_model.pt",
                                          image_path=self.output_dir_path+f'/images/{file}',
                                          image_size=640,
                                          confidence=.80,
                                          save_txt=True,
                                          save_img=True)

                seg.load_model()
                seg.run_segmentation()
                seg.get_segment_coordinates()
                print(self.output_dir_path + f'/{file}')
                seg.snip_articles()

    def run_pipeline(self) -> None:
        """
        This function runs through the entire image generation pipeline, from splitting PDFs to article segmentation.

        :return: None
        """

        self.split_pages()
        self.convert_pdfs_to_images()
        self.segment_images()