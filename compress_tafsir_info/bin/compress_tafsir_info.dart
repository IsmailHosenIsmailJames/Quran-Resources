import 'dart:convert';
import 'dart:developer';
import 'dart:io';

import 'package:archive/archive.dart';

void main(List<String> arguments) async {
  Directory spitedTafsirDataFolder = Directory("splited_tafsir_data");
  List<FileSystemEntity> filesList = spitedTafsirDataFolder.listSync();
  for (int index = 0; index < filesList.length; index++) {
    FileSystemEntity file = filesList[index];
    log("Possessing $index : ${file.path}", name: "File");

    var jsonFile = File(file.path);

    String jsonString = await jsonFile.readAsString();
    String compressedString = compressStringWithGZip(jsonString);
    await File("full_file_compression/${file.path.split("/").last}")
        .writeAsString(jsonEncode(compressedString));
    log("$index Done ${file.parent}", name: "Success");
  }
}

String compressStringWithGZip(String text) {
  final encoder = BZip2Encoder();
  final x = encoder.encode(utf8.encode(text));
  return base64.encode(x);
}

String decompressStringWithGZip(String compressedText) {
  final decoder = BZip2Decoder();
  final decompressedBytes = decoder.decodeBytes(base64Decode(compressedText));
  return utf8.decode(decompressedBytes);
}
