package com.example.xvideos.dao;

import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.Query;
import androidx.room.Update;

import com.example.xvideos.model.SinhVien;

import java.util.List;

@Dao
public interface SinhVienDao {
    @Query("select * from SinhVien")
    List<SinhVien> getAll();

    @Insert
    void insert(SinhVien sinhVien);

    @Update
    void update(SinhVien sinhVien);

    @Delete
    void delete(SinhVien sinhVien);
}
